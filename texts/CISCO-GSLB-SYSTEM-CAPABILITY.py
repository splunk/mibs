#
# PySNMP MIB module CISCO-GSLB-SYSTEM-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-GSLB-SYSTEM-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:45 2026
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
ciscoGslbSystemCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 534))
ciscoGslbSystemCapability.setRevisions(('2011-09-14 00:00', '2008-09-15 00:00', '2007-02-23 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoGslbSystemCapability.setRevisionsDescriptions(('Added ciscoGslbSystemCapabilityV04R01 agent\n        capabilities for Global Site Selector(GSS)\n        release 4.1.0.', 'Added ciscoGslbSystemCapabilityV03R00 agent\n        capabilities for Global Site Selector(GSS)\n        release 3.0.', 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoGslbSystemCapability.setLastUpdated('201109140000Z')
if mibBuilder.loadTexts: ciscoGslbSystemCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoGslbSystemCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal:  170 W Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel:  +1 800 553-NETS\n\n            E-mail:  cs-slb@cisco.com')
if mibBuilder.loadTexts: ciscoGslbSystemCapability.setDescription('The capabilities description\n        of CISCO-GSLB-SYSTEM-MIB.')
ciscoGslbSystemCapabilityV02R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 534, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbSystemCapabilityV02R00 = ciscoGslbSystemCapabilityV02R00.setProductRelease('GSS 2.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbSystemCapabilityV02R00 = ciscoGslbSystemCapabilityV02R00.setStatus('current')
if mibBuilder.loadTexts: ciscoGslbSystemCapabilityV02R00.setDescription('GSS 2.0 Cisco GSLB SYSTEM MIB capabilities')
ciscoGslbSystemCapabilityV03R00 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 534, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbSystemCapabilityV03R00 = ciscoGslbSystemCapabilityV03R00.setProductRelease('Global Site Selector(GSS) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbSystemCapabilityV03R00 = ciscoGslbSystemCapabilityV03R00.setStatus('current')
if mibBuilder.loadTexts: ciscoGslbSystemCapabilityV03R00.setDescription('GSS 3.0 Cisco GSLB SYSTEM MIB capabilities')
ciscoGslbSystemCapabilityV04R01 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 534, 3))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbSystemCapabilityV04R01 = ciscoGslbSystemCapabilityV04R01.setProductRelease('Global Site Selector(GSS) 4.1.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoGslbSystemCapabilityV04R01 = ciscoGslbSystemCapabilityV04R01.setStatus('current')
if mibBuilder.loadTexts: ciscoGslbSystemCapabilityV04R01.setDescription('GSS 4.1.0 Cisco GSLB SYSTEM MIB capabilities')
mibBuilder.exportSymbols("CISCO-GSLB-SYSTEM-CAPABILITY", ciscoGslbSystemCapabilityV03R00=ciscoGslbSystemCapabilityV03R00, ciscoGslbSystemCapability=ciscoGslbSystemCapability, PYSNMP_MODULE_ID=ciscoGslbSystemCapability, ciscoGslbSystemCapabilityV02R00=ciscoGslbSystemCapabilityV02R00, ciscoGslbSystemCapabilityV04R01=ciscoGslbSystemCapabilityV04R01)
