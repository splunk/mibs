#
# PySNMP MIB module CISCO-OTN-IF-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-OTN-IF-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:46 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "NotificationGroup", "ModuleCompliance")
Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, ModuleIdentity, MibIdentifier, iso, Counter32, IpAddress, Integer32, NotificationType, ObjectIdentity, Unsigned32, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "ModuleIdentity", "MibIdentifier", "iso", "Counter32", "IpAddress", "Integer32", "NotificationType", "ObjectIdentity", "Unsigned32", "Bits", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoOtnIfMIBCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 562))
ciscoOtnIfMIBCapability.setRevisions(('2007-10-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoOtnIfMIBCapability.setRevisionsDescriptions(('First version of this MIB module.',))
if mibBuilder.loadTexts: ciscoOtnIfMIBCapability.setLastUpdated('200710200000Z')
if mibBuilder.loadTexts: ciscoOtnIfMIBCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoOtnIfMIBCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n\n            Postal: 170 W Tasman Drive\n\n            San Jose, CA  95134\n\n            USA\n\n\n            Tel: +1 800 553-NETS\n\n\n            E-mail: cs-dwdm-mibs@cisco.com')
if mibBuilder.loadTexts: ciscoOtnIfMIBCapability.setDescription('capabilities description for CISCO-OTN-IF-MIB')
ciscoOtnIfCapIOSXRV3R06CRS1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 562, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOtnIfCapIOSXRV3R06CRS1 = ciscoOtnIfCapIOSXRV3R06CRS1.setProductRelease('Cisco IOS-XR Release 3.6 for CRS-1')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoOtnIfCapIOSXRV3R06CRS1 = ciscoOtnIfCapIOSXRV3R06CRS1.setStatus('current')
if mibBuilder.loadTexts: ciscoOtnIfCapIOSXRV3R06CRS1.setDescription('Cisco OTN IF MIB capabilities for IOX-XR Release 3.6 for CRS 1')
mibBuilder.exportSymbols("CISCO-OTN-IF-CAPABILITY", PYSNMP_MODULE_ID=ciscoOtnIfMIBCapability, ciscoOtnIfCapIOSXRV3R06CRS1=ciscoOtnIfCapIOSXRV3R06CRS1, ciscoOtnIfMIBCapability=ciscoOtnIfMIBCapability)
