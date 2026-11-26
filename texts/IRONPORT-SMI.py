#
# PySNMP MIB module IRONPORT-SMI (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/IRONPORT-SMI
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:46 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, TimeTicks, MibIdentifier, enterprises, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "TimeTicks", "MibIdentifier", "enterprises", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ironPort = ModuleIdentity((1, 3, 6, 1, 4, 1, 15497))
ironPort.setRevisions(('2011-05-02 16:00', '2005-06-17 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ironPort.setRevisionsDescriptions(('Cleaned up SMI definition.', 'Initial revision.',))
if mibBuilder.loadTexts: ironPort.setLastUpdated('201105021600Z')
if mibBuilder.loadTexts: ironPort.setOrganization('IronPort Systems')
if mibBuilder.loadTexts: ironPort.setContactInfo('       Cisco IronPort Email and Web Security\n                Customer Service\n\n        Postal: 950 Elm Avenue\n                San Bruno, CA 94066\n                USA\n\n           Tel: +1 (650) 989-6533\n\n        E-mail: customercare@ironport.com')
if mibBuilder.loadTexts: ironPort.setDescription('Top-level infrastructure of the Cisco IronPort project\n         enterprise MIB tree.')
asyncOSAppliances = MibIdentifier((1, 3, 6, 1, 4, 1, 15497, 1))
asyncOSMail = MibIdentifier((1, 3, 6, 1, 4, 1, 15497, 1, 1))
mibBuilder.exportSymbols("IRONPORT-SMI", asyncOSMail=asyncOSMail, PYSNMP_MODULE_ID=ironPort, asyncOSAppliances=asyncOSAppliances, ironPort=ironPort)
