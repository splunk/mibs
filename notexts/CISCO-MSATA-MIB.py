#
# PySNMP MIB module CISCO-MSATA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-MSATA-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity, IpAddress, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity", "IpAddress", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMsataMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 860))
ciscoMsataMIB.setRevisions(('2019-01-09 00:00',))
if mibBuilder.loadTexts: ciscoMsataMIB.setLastUpdated('201901090000Z')
if mibBuilder.loadTexts: ciscoMsataMIB.setOrganization('Cisco Systems, Inc.')
ciscoMsataMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 860, 0))
ciscoMsata = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 860, 0, 1), OctetString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ciscoMsata.setStatus('current')
mibBuilder.exportSymbols("CISCO-MSATA-MIB", ciscoMsata=ciscoMsata, ciscoMsataMIB=ciscoMsataMIB, ciscoMsataMIBObjects=ciscoMsataMIBObjects, PYSNMP_MODULE_ID=ciscoMsataMIB)
