#
# PySNMP MIB module IRONPORT-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/IRONPORT-SMI
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:00 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter64, TimeTicks, NotificationType, Integer32, iso, enterprises, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Gauge32, Unsigned32, MibIdentifier, Counter32, ObjectIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "NotificationType", "Integer32", "iso", "enterprises", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Gauge32", "Unsigned32", "MibIdentifier", "Counter32", "ObjectIdentity", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ironPort = ModuleIdentity((1, 3, 6, 1, 4, 1, 15497))
ironPort.setRevisions(('2011-05-02 16:00', '2005-06-17 00:00',))
if mibBuilder.loadTexts: ironPort.setLastUpdated('201105021600Z')
if mibBuilder.loadTexts: ironPort.setOrganization('IronPort Systems')
asyncOSAppliances = MibIdentifier((1, 3, 6, 1, 4, 1, 15497, 1))
asyncOSMail = MibIdentifier((1, 3, 6, 1, 4, 1, 15497, 1, 1))
mibBuilder.exportSymbols("IRONPORT-SMI", PYSNMP_MODULE_ID=ironPort, ironPort=ironPort, asyncOSAppliances=asyncOSAppliances, asyncOSMail=asyncOSMail)
