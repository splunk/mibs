#
# PySNMP MIB module CISCO-IP-PROTOCOL-FILTER-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/cisco/CISCO-IP-PROTOCOL-FILTER-CAPABILITY
# Produced by pysmi-1.1.12 at Thu Nov 26 06:07:44 2026
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
ciscoIpProtFilterCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 500))
ciscoIpProtFilterCapability.setRevisions(('2008-06-09 00:00', '2006-04-19 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIpProtFilterCapability.setRevisionsDescriptions(('Added capability statement\n        cIpProtFilterCapc4710aceVA1R700 for ACE 4710 \n        Application Control Engine Appliance.', 'Added capability statement\n        cIpProtFilterCapACSWV03R000 \n        for Application Control Engine (ACE).',))
if mibBuilder.loadTexts: ciscoIpProtFilterCapability.setLastUpdated('200806090000Z')
if mibBuilder.loadTexts: ciscoIpProtFilterCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIpProtFilterCapability.setContactInfo('Cisco Systems\n            Customer Service\n\n            Postal: 170 West Tasman Drive\n            San Jose, CA  95134\n            USA\n\n            Tel: +1 800 553-NETS\n\n            E-mail: cs-dot11@cisco.com')
if mibBuilder.loadTexts: ciscoIpProtFilterCapability.setDescription('The capabilities description for\n        CISCO-IP-PROTOCOL-FILTER-MIB.')
cIpProtFilterCapACSWV03R000 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 500, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpProtFilterCapACSWV03R000 = cIpProtFilterCapACSWV03R000.setProductRelease('ACSW (Application Control Software) 3.0')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpProtFilterCapACSWV03R000 = cIpProtFilterCapACSWV03R000.setStatus('current')
if mibBuilder.loadTexts: cIpProtFilterCapACSWV03R000.setDescription('CISCO-IP-PROTOCOL-FILTER-MIB capabilities.')
cIpProtFilterCapc4710aceVA1R700 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 500, 2))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpProtFilterCapc4710aceVA1R700 = cIpProtFilterCapc4710aceVA1R700.setProductRelease('ACSW (Application Control Software) A1(7)\n                  for ACE 4710 Application Control Engine \n                  Appliance.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cIpProtFilterCapc4710aceVA1R700 = cIpProtFilterCapc4710aceVA1R700.setStatus('current')
if mibBuilder.loadTexts: cIpProtFilterCapc4710aceVA1R700.setDescription('CISCO-IP-PROTOCOL-FILTER-MIB capabilities.')
mibBuilder.exportSymbols("CISCO-IP-PROTOCOL-FILTER-CAPABILITY", PYSNMP_MODULE_ID=ciscoIpProtFilterCapability, ciscoIpProtFilterCapability=ciscoIpProtFilterCapability, cIpProtFilterCapc4710aceVA1R700=cIpProtFilterCapc4710aceVA1R700, cIpProtFilterCapACSWV03R000=cIpProtFilterCapACSWV03R000)
