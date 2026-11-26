#
# PySNMP MIB module CISCOSB-WeightedRandomTailDrop-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCOSB-WeightedRandomTailDrop-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
switch001, = mibBuilder.importSymbols("CISCOSB-MIB", "switch001")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rlWeightedRandomTailDrop = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 146))
rlWeightedRandomTailDrop.setRevisions(('2009-09-29 00:00',))
if mibBuilder.loadTexts: rlWeightedRandomTailDrop.setLastUpdated('200909290000Z')
if mibBuilder.loadTexts: rlWeightedRandomTailDrop.setOrganization('Cisco Systems, Inc.')
rlWeightedRandomTailDropCurrentStatus = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 146, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("enable", 0), ("disable", 1)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlWeightedRandomTailDropCurrentStatus.setStatus('current')
rlWeightedRandomTailDropStatusAfterReset = MibScalar((1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 146, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1))).clone(namedValues=NamedValues(("enable", 0), ("disable", 1)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlWeightedRandomTailDropStatusAfterReset.setStatus('current')
mibBuilder.exportSymbols("CISCOSB-WeightedRandomTailDrop-MIB", rlWeightedRandomTailDropCurrentStatus=rlWeightedRandomTailDropCurrentStatus, rlWeightedRandomTailDrop=rlWeightedRandomTailDrop, rlWeightedRandomTailDropStatusAfterReset=rlWeightedRandomTailDropStatusAfterReset, PYSNMP_MODULE_ID=rlWeightedRandomTailDrop)
