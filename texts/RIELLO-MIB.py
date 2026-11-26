#
# PySNMP MIB module RIELLO-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/riello/RIELLO-MIB
# Produced by pysmi-1.1.12 at Thu Nov 26 06:14:17 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, enterprises, Bits, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter64, ModuleIdentity, Gauge32, NotificationType, Counter32, iso, MibIdentifier, Integer32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "enterprises", "Bits", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter64", "ModuleIdentity", "Gauge32", "NotificationType", "Counter32", "iso", "MibIdentifier", "Integer32", "IpAddress")
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
