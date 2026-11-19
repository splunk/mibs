#
# PySNMP MIB module RIELLO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/riello/RIELLO-MIB
# Produced by pysmi-1.1.12 at Thu Nov 19 08:39:35 2026
# On host runnervmccnms platform Linux version 7.0.0-1019-azure by user runner
# Using Python version 3.11.18 (main, Oct 26 2026, 02:48:29) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, NotificationType, iso, ObjectIdentity, IpAddress, TimeTicks, Gauge32, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, MibIdentifier, Integer32, Counter64, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "NotificationType", "iso", "ObjectIdentity", "IpAddress", "TimeTicks", "Gauge32", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "MibIdentifier", "Integer32", "Counter64", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rielloMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 5491))
rielloMIB.setRevisions(('2016-02-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rielloMIB.setRevisionsDescriptions(('Latest avaialble',))
if mibBuilder.loadTexts: rielloMIB.setLastUpdated('201602230000Z')
if mibBuilder.loadTexts: rielloMIB.setOrganization('RPS S.p.A')
if mibBuilder.loadTexts: rielloMIB.setContactInfo('        Michele Marcon\n             E-mail: info@riello-ups.com')
if mibBuilder.loadTexts: rielloMIB.setDescription('The MIB module to describe Riello devices.')
mibBuilder.exportSymbols("RIELLO-MIB", PYSNMP_MODULE_ID=rielloMIB, rielloMIB=rielloMIB)
