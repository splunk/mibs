#
# PySNMP MIB module PAN-GLOBAL-REG (http://snmplabs.com/pysmi)
# ASN.1 source file:///home/runner/work/mibs/mibs/src/vendor/paloaltonetworks/PAN-GLOBAL-REG
# Produced by pysmi-1.1.12 at Thu Nov 26 06:13:14 2026
# On host runnervm0hi8g platform Linux version 7.0.0-1020-azure by user runner
# Using Python version 3.13.18 (main, Oct 26 2026, 14:19:33) [GCC 15.2.0]
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, TimeTicks, MibIdentifier, Counter32, ObjectIdentity, Unsigned32, ModuleIdentity, enterprises, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, NotificationType, Bits, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "TimeTicks", "MibIdentifier", "Counter32", "ObjectIdentity", "Unsigned32", "ModuleIdentity", "enterprises", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "NotificationType", "Bits", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
panGlobalRegModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 25461, 1, 1, 1))
panGlobalRegModule.setRevisions(('2011-02-09 16:10',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: panGlobalRegModule.setRevisionsDescriptions(('\n\t\t\tRev 1.0\n\t\t\tInitial version of MIB module PAN-GLOBAL-REG.',))
if mibBuilder.loadTexts: panGlobalRegModule.setLastUpdated('201106271040Z')
if mibBuilder.loadTexts: panGlobalRegModule.setOrganization('Palo Alto Networks')
if mibBuilder.loadTexts: panGlobalRegModule.setContactInfo('\n\t\t\t\t\tCustomer Support\n\t\t\t\t\tPalo Alto Networks\n\t\t\t\t\t4401 Great America Pkwy\n\t\t\t\t\tSanta Clara, CA 95054-1211\n\n\t\t\t\t\t+1 866-898-9087\n\t\t\t\t\tsupport at paloaltonetworks dot com')
if mibBuilder.loadTexts: panGlobalRegModule.setDescription("\n\t\t\tA MIB module containing top-level OID definitions\n\t\t\tfor various sub-trees for Palo Alto Networks' enterprise MIB modules.")
panRoot = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461))
if mibBuilder.loadTexts: panRoot.setStatus('current')
if mibBuilder.loadTexts: panRoot.setDescription('\n\t\t\tThe root of the OID sub-tree assigned to Palo Alto Networks assigned by\n\t\t\tthe Internet Assigned Numbers Authority (IANA).')
panReg = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 1))
if mibBuilder.loadTexts: panReg.setStatus('current')
if mibBuilder.loadTexts: panReg.setDescription('\n\t\t\tSub-tree for registrations - identification of modules and logical and\n\t\t\tphysical components.')
panModules = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 1, 1))
if mibBuilder.loadTexts: panModules.setStatus('current')
if mibBuilder.loadTexts: panModules.setDescription('\n\t\t\tSub-tree for module registrations.')
panMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2))
if mibBuilder.loadTexts: panMibs.setStatus('current')
if mibBuilder.loadTexts: panMibs.setDescription('\n\t\t\tSub-tree for all Palo Alto object and event definitions.')
panCommonMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 1))
if mibBuilder.loadTexts: panCommonMib.setStatus('current')
if mibBuilder.loadTexts: panCommonMib.setDescription('\n\t\t\tSub-tree for common Palo Alto object and event definitions.\n\t\t\tThese would be implemented by all Palo Alto products.')
panSpecificMib = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 2))
if mibBuilder.loadTexts: panSpecificMib.setStatus('current')
if mibBuilder.loadTexts: panSpecificMib.setDescription('\n\t\t\tSub-tree for specific Palo Alto object and event definitions.')
panProductsMibs = ObjectIdentity((1, 3, 6, 1, 4, 1, 25461, 2, 3))
if mibBuilder.loadTexts: panProductsMibs.setStatus('current')
if mibBuilder.loadTexts: panProductsMibs.setDescription('\n\t\t\tSub-tree for all Palo Alto product specific definitions.')
mibBuilder.exportSymbols("PAN-GLOBAL-REG", panModules=panModules, panSpecificMib=panSpecificMib, panRoot=panRoot, panGlobalRegModule=panGlobalRegModule, panMibs=panMibs, PYSNMP_MODULE_ID=panGlobalRegModule, panCommonMib=panCommonMib, panProductsMibs=panProductsMibs, panReg=panReg)
